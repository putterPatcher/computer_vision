from cv2.typing import MatLike
from terminate import retrn
from ..__helpers import invalid_command

class ClusterDetection:
    def __init__(self,__a:MatLike,ret='c'):
        try:
            if __a.__class__.__name__=='MatLike':self.__a=__a;self.__points_array=self.__mask_to_points_array(__a);
            else:raise Exception
        except Exception as e:invalid_command('ClusterDetection');retrn(ret,e);

    def __mask_to_points_array(self,__a:MatLike):
        points = []
        for i in range(__a.shape[0]):
            for j in range(__a.shape[1]):
                if __a[i][j] == 1:points.append((i,j))

    def get_clusters(self, method='dbscan'):
        pass

