from analyticsconfig import ConfigFacade

c = ConfigFacade()
print(c.get_secret('asd', default='123'))