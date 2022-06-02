from intSampling import intSampling
from strSampling import strSampling
from selfDefinedStructSampling import selfDefinedStructSampling
from selfDefinedClassSampling import selfDefinedClassSampling


class dataFactoryInterface(object):
    def __init__(self):
        self.name="datafactoryinterface"

    def create(self,target):
        classname=target + "Sampling"
        return eval(classname)()
