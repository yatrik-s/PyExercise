# Testing ImportError exception
try:
    import NonExistingModule
except ImportError:
    print 'Module does not exists...exiting'
