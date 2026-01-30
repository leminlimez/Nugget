from pymobiledevice3.lockdown import LockdownClient

def get_model_name(product_type: str) -> str:
    return "iPhone something"

def get_idiom(device_class: str) -> str:
    if device_class == 'iPhone':
        return 'phone'
    else:
        return 'pad'

def generate_mga(ld: LockdownClient) -> dict:
    # queries the device values and generates a mobile gestalt dictionary to return
    vals = ld.all_values
    prod = vals['ProductType']
    device_class = vals['DeviceClass']
    region = vals['RegionInfo'].split("/")
    build = vals['BuildVersion']
    model_name = get_model_name(prod)
    cache_extra = {
        # main dict to query
        "+3Uf0Pm5F8Xy7Onyvko0vA": device_class,                     # DeviceClass
        "/YYygAofPDbhrwToVsXdeA": vals['HardwareModel'],            # HardwareModel
        "0+nc/Udy4WNG8S+Q7a/s1A": prod,                             # ProductType
        # "0GizaJLOyfzgAbxQ/5aniA"                                  ## DeviceHousingColorUncooked
        # "4W7X4OWHjri5PGaAGsCWxw"                                  ## MaxH264PlaybackLevel
        # "4qfpxrvLtWillIHpIsVgMA"                                  ## SystemImageID
        "5pYKlGnYYBzGvAlIU8RjEQ": vals['HardwarePlatform'],         # HardwarePlatform
        # "913P3Zsei09w0GSSOaBD+w"                                  ## VolumeUpButtonNormalizedCGRect
        "91LyMcx4z1w3SGVeqteMnA": vals['BasebandRegionSKU'],        # BasebandRegionSKU
        # "96GRvvjuBKkU4HzNsYcHPA"                                  ## MinimumSupportediTunesVersion
        # "97JDvERpVwO+GHtthIh7hA"                                  ## RegulatoryModelNumber
        "9MZ5AdH43csAUajl/dU+IQ": vals['SupportedDeviceFamilies'],  # SupportedDeviceFamilies
        "9s45ldrCC1WF+7b6C4H2BA": prod,                             # GSDeviceName
        # "AoKnINTLPoKML3ctoP0AZg"                                  ## IOSurfaceFormatDictionary
        "DViRIxZ/ZwO007CLcEYvZw": "",                               # DViRIxZ/ZwO007CLcEYvZw
        # "HXTqT3UXOKuTEklxz+wMAA"                                  ## BasebandAPTimeSync
        "IMLaTlxS7ITtwfbRfPYWuA": region[1],                        # DeviceVariantGuess
        # "J1QHVh74Nnd6Rqyiq71/yw"                                  ## AVDDecodingRate
        # "JHXk7RXOxvlqK+SxkwcM2A"                                  ## LowPowerExpressModesSupported
        "JUWcn+5Ss0nvr5w/jk4WEg": device_class,                     # device-name
        # "JhEU414EIaDvAz8ki5DSqw"                                  ## DeviceEnclosureColor
        # "LTI8wHvEYKy8zR1IXBW1uQ"                                  ## ArtworkTraitDisplayGamut
        "LeSRsiLoJCMhjn6nd6GWbQ": vals['FirmwareVersion'],          # FirmwareVersion
        # "NUYAz1eq3Flzt7ZQxXC/ng"                                  ## FirstPartyLaunchTimeLimitScale
        # "NaA/zJV7myg2w4YNmSe4yQ"                                  ## WifiChipset
        # "Nzu4E/VsXjEIa83CkRdZrQ"                                  ## Image4CryptoHashMethod
        # "PdprWthPO6YyrO6p1vLRgQ"                                  ## VolumeDownButtonCGRect
        # "QbQzuIbef01P4JeoL9EmKg"                                  ## DeviceSceneUpdateTimeLimitScale
        # "SbXytSPZXB1jQ8GLZOxCPw"                                  ## VolumeDownButtonNormalizedCGRect
        # "TZ/0j62wM3D0CuRt+Nc/Lw"                                  ## ProductHash
        # "VuGdqp8UBpi9vPWHlPluVQ"                                  ## CompatibleAppVariants
        # "WPEkba78QeFFU/wgqpOx6w"                                  ## UserIntentPhysicalButtonNormalizedCGRect
        "Z/dqyWS6OZTRy10UcmUAhw": model_name,                       # marketing-name
        # "aD51uqjUwgRKjAC04BCrxg"                                  ## VolumeUpButtonCGRect
        "bbtR9jQx50Fv5Af/affNtA": model_name,                       # PhysicalHardwareNameString
        # "c7fCSBIbX1mFaRoKT5zTIw"                                  ## WifiVendor
        # "emXA9B552rnSoI7xXE91DA"                                  ## DeviceLaunchTimeLimitScale
        # "gBw7IWiBnLHaA+lBrZBgWw"                                  ## CameraMaxBurstLength
        # "gD8SNRcHQeIxCAvsp+2vjA"                                  ## WSKU
        "h63QSdBCiT/z0WU6rdQv6Q": region[0],                        # RegionCode
        "h9jDsbgj7xIVeIQ8S3/X3Q": prod,                             # ProductType
        "ivIu8YTDnBSrYv/SN4G8Ag": vals['ProductName'],              # ProductName
        # "k+KTni1jrwErpcDMEnn3aw"                                  ## MobileDeviceMinimumVersion
        "k7QIBwZJJOVw+Sej/8h8VA": vals['CPUArchitecture'],          # CPUArchitecture
        "mZfUC7qo4pURNhyMHZ62RQ": build,                            # BuildVersion
        "mumHZHMLEfAuTkkd28fHlQ": vals['DeviceColor'],              # DeviceColor
        # "nSo8opze5rFk+EdBoR6tBw"                                  ## RestrictedCountryCodes
        # "oBbtJ8x+s1q0OkaiocPuog"                                  ## MainScreenStaticInfo
        "oPeik/9e8lQWMszEjbPzng": {                                 # ArtworkTraits
            "ArtworkDeviceIdiom": get_idiom(device_class),
            "ArtworkDeviceProductDescription": model_name,
            # "ArtworkDeviceScaleFactor"
            # "ArtworkDeviceSubType"
            # "ArtworkDisplayGamut"
            # "ArtworkDynamicDisplayMode"
            # "CompatibleDeviceFallback"
            # "DevicePerformanceMemoryClass"
            # "GraphicsFeatureSetClass"
            # "GraphicsFeatureSetFallbacks"
        },
        "oYicEKzVTz4/CxxE05pEgQ": vals['HardwareModel'],            # TargetSubType
        # "pB5sZVvnp+QjZQtt2KfQvA"                                  ## BasebandChipset
        # "pMeQxE5szZTjLMk10TisDQ"                                  ## UserIntentPhysicalButtonCGRect
        "qNNddlUK+B/YlooNoymwgA": vals['ProductVersion'],           # ProductVersion
        # "qwXfFvH5jPXPxrny0XuGtQ"                                  ## BuildID
        # "rJkMAGeVLdhP5+10G5hVcA"                                  ## UserIntentPhysicalButtonCGRectString
        "rkqlwPcRHwixY4gapPjanw": device_class,                     # DeviceName
        "vme9Buk6XiWFCXoHApxNFA": device_class,                     # MarketingDeviceFamilyName
        # "wYMBabAO8VguyDDVgCsPdg"                                  ## WiFiChipsetRevision
        "xUHcyT2/HE8oi/4LaOI+Sw": vals['PartitionType'],            # PartitionType
        # "xojWvSTQWT7Icy+xfVzjAQ"                                  ## FramebufferIdentifier
        # "yUqD8AXE/c+IggkuYoxrqA"                                  ## ChromeIdentifier
        # "ybGkijAwLTwevankfVzsDQ"                                  ## MainScreenCanvasSizes
        "yjP8DgByZmLk04Ta6f6DWQ": "iOS",                            # PartitionStyle
        "zHeENZu+wbg7PUprwNwBWg": vals['RegionInfo'],               # RegionInfo
    }
    return {
        # "CacheData": b"",
        "CacheExtra": cache_extra,
        # "CacheUUID": "",
        "CacheVersion": build # build number
    }