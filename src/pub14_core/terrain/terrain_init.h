// This file is part of SWGANH which is released under the MIT license.
// See file LICENSE or go to http://swganh.com/LICENSE
#pragma once

#include <boost/program_options/options_description.hpp>
#include <boost/program_options/variables_map.hpp>

#include "anh/logger.h"

#include "anh/plugin/bindings.h"
#include "anh/plugin/plugin_manager.h"

#include "swganh/app/swganh_kernel.h"

#include "terrain_service.h"

#include "version.h"

namespace swganh_core {
namespace terrain {

inline void Initialize(swganh::app::SwganhKernel* kernel) 
{    
    anh::plugin::ObjectRegistration registration;
    registration.version.major = VERSION_MAJOR;
    registration.version.minor = VERSION_MINOR;

	// Register
    registration.CreateObject = [kernel] (anh::plugin::ObjectParams* params) -> void * {
        return new TerrainService(kernel);
    };

    registration.DestroyObject = [] (void * object) {
        if (object) {
            delete static_cast<TerrainService*>(object);
        }
    };

    kernel->GetPluginManager()->RegisterObject("Terrain::TerrainService", &registration);    

}

}}  // namespace swganh_core::galaxy