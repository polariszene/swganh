// This file is part of SWGANH which is released under the MIT license.
// See file LICENSE or go to http://swganh.com/LICENSE
#pragma once

#include <glm/glm.hpp>

#include "swganh_core/object/intangible/intangible.h"

namespace swganh {
namespace object {

class CellFactory;
class CellMessageBuilder;
class Cell : public swganh::object::Intangible {

public:
	typedef CellFactory FactoryType;
	typedef CellMessageBuilder MessageBuilderType;
    // SCLT
    virtual uint32_t GetType() const { return Cell::type; }
    const static uint32_t type = 0x53434c54;

    /**
    * @brief Gets the current cell number
    *   @returns cell number
    */
    uint32_t GetCell();

    /**
    * @brief sets the current cell number
    *   @param cell number
    */
    void SetCell(uint32_t cell_number);

	virtual std::shared_ptr<Object> Clone();
	void Clone(std::shared_ptr<Cell> other);

};

}} // swganh::object
