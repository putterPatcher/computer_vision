from cv2.typing import MatLike
from terminate import retrn
from ..__helpers import invalid_command

class ClusterDetection:
    def __init__(self,__a:MatLike,ret='c'):
        try:
            if __a.__class__.__name__=='MatLike':self.__a=__a;
            else:raise Exception
        except Exception as e:invalid_command('ClusterDetection');retrn(ret,e);

    def get_clusters(self):
        pass