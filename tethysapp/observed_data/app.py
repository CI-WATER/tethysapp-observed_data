from tethys_apps.base import TethysAppBase, url_map_maker
from tethys_apps.base import PersistentStore

class ObservedHydrologicData(TethysAppBase):
    """
    Tethys app class for Observed Hydrologic Data.
    """

    name = 'Observed Hydrologic Data'
    index = 'observed_data:home'
    icon = 'observed_data/images/logo.png'
    package = 'observed_data'
    root_url = 'observed-data'
    color = '#e67e22'
        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='observed-data',
                           controller='observed_data.controllers.home'),              
                    UrlMap(name='plot',
                           url='observed-data/plot',
                           controller='observed_data.controllers.plot'
                           )
        )

        return url_maps





