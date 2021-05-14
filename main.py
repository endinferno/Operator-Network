import Interface
import Factory


def main():
    factory = Factory.Factory()
    interface = Interface.Interface()
    interface.defineModule()
    interface.initOperator(factory)
    interface.initAction()
    interface.packModule()
    interface.Run()


if __name__ == '__main__':
    main()
