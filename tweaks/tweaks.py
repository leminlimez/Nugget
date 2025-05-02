from devicemanagement.constants import Version
from .tweak_classes import MobileGestaltTweak, MobileGestaltMultiTweak, MobileGestaltPickerTweak, FeatureFlagTweak, BasicPlistTweak, AdvancedPlistTweak, RdarFixTweak, NullifyFileTweak
from .eligibility_tweak import EligibilityTweak, AITweak
from .posterboard.posterboard_tweak import PosterboardTweak
from .posterboard.template_options.templates_tweak import TemplatesTweak
from .status_bar.status_bar_tweak import StatusBarTweak
from .basic_plist_locations import FileLocation
    
tweaks = {
    ## PosterBoard
    "PosterBoard": PosterboardTweak(),

    ## Templates
    "Templates": TemplatesTweak(),

    ## Status Bar
    "StatusBar": StatusBarTweak()
}