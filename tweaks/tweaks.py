from devicemanagement.constants import Version
from .tweak_names import TweakID
from .tweak_classes import MobileGestaltTweak, MobileGestaltMultiTweak, MobileGestaltPickerTweak, FeatureFlagTweak, BasicPlistTweak, AdvancedPlistTweak, RdarFixTweak, NullifyFileTweak
from .eligibility_tweak import EligibilityTweak, AITweak
from .posterboard.posterboard_tweak import PosterboardTweak
from .posterboard.template_options.templates_tweak import TemplatesTweak
from .status_bar.status_bar_tweak import StatusBarTweak
from .passcode_theme_tweak import PasscodeThemeTweak
from .basic_plist_locations import FileLocation
    
tweaks = {
    ## PosterBoard
    TweakID.PosterBoard: PosterboardTweak(),

    ## Templates
    TweakID.Templates: TemplatesTweak(),

    ## Status Bar
    TweakID.StatusBar: StatusBarTweak(),

    ## Passcode Theme
    TweakID.Passcode: PasscodeThemeTweak()
}