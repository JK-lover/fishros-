# 使用colcon功能包组织节点注意事项

1. colcon list/build的路径必须是node_package的同一路径 
2. 提示 no package finished，可以删除隐藏忽略文件 find src -name COLCON_IGNORE -delete 
3. package.xml 中 <name>demo_cpp_pkg</name> CMakeLists.txt 中 project(demo_cpp_pkg)必须一致 
4. 在以后的操作中，不要永久写入 .bashrc，而是在需要时手动激活） 
5. ament_package()在cmakelist里要放到最后 
6. ament_cmake 是构建工具依赖，通常需要放在其他依赖之前。详情见/p2/src/demo_cpp_pkg/package.xml
7. 若多功能包需要依赖关系，则在后者的package.xml的依赖中加入<depend>demo_cpp_pkg</depend>