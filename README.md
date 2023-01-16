# RGBD-multiview_3D-registration
This is the next version for RGBD-multiview 3D-registration. (algorithm improvement)

- subject : RGBD-multiview 3D-registration
- equipment : MS Azure kinect
- library : pykinect, opencv, open3d, numpy
- source code\
  cal_RT.py : RGBD capturing, calculationg 3d transformation matrix (least squares method)\
  pc_combine.py : registration process of point-clouds using calculated transformation matrix\
  py_play.py : visualization of registrated point-clouds\
  remove_all.py : removing all of generated files from previous run
- files\
  pykinect_azure : pykinect library\
  color : captured color image\
  trns_color : color image mapped to depth map\
  pc : captured point-clouds (before registration)\
  rt : calculated transformation matrix\
  fin_pc : transformed point-clouds
 - how to test\
  add libraries\
  connect azure kinect\
  run cal_RT.py and pc_combine.py sequentially
  
Improvements
  1. replaced with accurate feature detector and matcher
  2. reduced accumulated point-cloud transforming time by using matrix chain product
  3. additional minor code fix to reduce execution time and improve accuracy
