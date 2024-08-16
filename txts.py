base_CMakeLists = """cmake_minimum_required(VERSION 3.25.0)
project(main VERSION 0.1.0 LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(main main.cpp)
#target_link_libraries(main )
"""

qt6_CMakeLists = """cmake_minimum_required(VERSION 3.25.0)
project(main VERSION 0.1.0 LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

#procura o qt6
find_package(Qt6 REQUIRED COMPONENTS Widgets)

add_executable(main main.cpp)

#inclui os diretorios de cabeçalho do qt
target_include_directories(main PRIVATE ${Qt6Widgets_INCLUDE_DIRS})

target_link_libraries(main PRIVATE Qt6::Widgets)
"""

base_main_cpp ="""#include <QApplication>
#include <QWidget>
#include <QtWidgets>

int main(int argc, char *argv[]) {
  QApplication app(argc, argv);
  QWidget window;
  window.resize(250, 150);
  window.setWindowTitle("Qt Exemplo");
  window.show();
  return app.exec();
}

"""
