from .SD_common.SD_DIG import SD_DIG

class Keysight_M3102A(SD_DIG):
    """
    qcodes driver for the Keysight M3102A Digitizer PXIe card.

    M3102A channel numbers start with 1.

    This driver is derived from SD_DIG

    Example:
        TODO

    Args:
        name: name for this instrument, passed to the base instrument
        chassis: chassis number where the device is located
        slot: slot number where the device is plugged in
    """
    def __init__(self, name: str, chassis: int, slot: int, **kwargs):
        super().__init__(name, chassis, slot, channels=4, triggers=8, **kwargs)

        module_name = "M3102A"
        if self.module_name != module_name:
            raise Exception(f"Found module '{self.module_name}' in chassis "
                            f"{chassis} slot {slot}; expected '{module_name}'")
