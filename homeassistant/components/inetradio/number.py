"""Numbers for inetradio."""

from homeassistant.components.number import NumberEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import INetRadioConfigEntry


async def async_setup_entry(
    hass: HomeAssistant,
    entry: INetRadioConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Volume setup."""
    async_add_entities([VolumeEntity(hass, entry)], update_before_add=True)


class VolumeEntity(NumberEntity):
    """Volume entity."""

    def __init__(self, hass: HomeAssistant, entry: INetRadioConfigEntry) -> None:
        """Init volume ent."""
        super().__init__()
        self._hass = hass
        self._config = entry
        self.name = "Volume"
        self.entity_id = "iNetRadio.Volume"

    async def async_update(self) -> None:
        """Async update."""
        self.native_value = 3
