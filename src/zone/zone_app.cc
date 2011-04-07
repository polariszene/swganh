/*
---------------------------------------------------------------------------------------
This source file is part of SWG:ANH (Star Wars Galaxies - A New Hope - Server Emulator)

For more information, visit http://www.swganh.com

Copyright (c) 2006 - 2010 The SWG:ANH Team */
#include "zone_app.h"
#include <iostream>

#include <boost/thread/thread.hpp>
#include <anh/module_manager/platform_services.h>

using namespace std;
using namespace anh;
using namespace scripting;
using namespace component;
using namespace event_dispatcher;
using namespace module_manager;

namespace zone {
ZoneApp::ZoneApp(int argc, char* argv[], list<string> config_files
    , shared_ptr<EventDispatcherInterface> dispatcher
    , shared_ptr<ScriptingManagerInterface> scripting_manager
    , shared_ptr<ModuleManager> module_manager)
    : BaseApplication(argc, argv, config_files, dispatcher, nullptr, scripting_manager, nullptr, module_manager) 
{
    auto startupListener = [&] (shared_ptr<EventInterface> incoming_event)-> bool {
        cout << "Zone Application Startup" <<endl;
        started_ = true;
        return true;
    };
    auto processListener = [] (shared_ptr<EventInterface> incoming_event)-> bool {
        cout << "Zone Application Process" <<endl;
        return true;
    };
    auto shutdownListener = [] (shared_ptr<EventInterface> incoming_event)-> bool {
        cout << "Zone Application Shutdown" <<endl;
        return true;
    };
}
ZoneApp::~ZoneApp() {
    //destructor
}
void ZoneApp::onAddDefaultOptions_() {
    cout<<"default options called" <<endl;
}
void ZoneApp::onRegisterApp_() {
    cout<<"on register app called" <<endl;
}
} //namespace zone
using namespace zone;
int main(int argc, char* argv[])
{
    // config files
    list<string> config;
    config.push_back("config/general.cfg");
    auto dispatcher = make_shared<EventDispatcher>();
    auto scripter = make_shared<ScriptingManager>("scripts");
    auto services = make_shared<module_manager::PlatformServices>();
    // add services
    services->addService("EventDispatcher", dispatcher);
    services->addService("ScriptingManager", scripter);
    
    auto module_manager = make_shared<ModuleManager>(services);
    ZoneApp app(argc, argv, config, dispatcher, scripter, module_manager);
    
    app.startup();
    boost::this_thread::sleep(boost::posix_time::milliseconds(5));
    if (app.hasStarted()) {
        while(true){
            app.process();
            if(cin.get() == 'q')
            {
                app.shutdown();
            }
        }
    }
    return 0;
}