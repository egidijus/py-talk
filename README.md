# simple python talky recognition thingy made by jason vogel

# How
```
make build
make run
```
If you receive this error during make build 


    ERROR: running install
    running build
    running build_py
    creating build
    creating build/lib.linux-x86_64-3.6
    copying src/pyaudio.py -> build/lib.linux-x86_64-3.6
    running build_ext
    building '_portaudio' extension
    creating build/temp.linux-x86_64-3.6
    creating build/temp.linux-x86_64-3.6/src
    x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -I/usr/include/python3.6m -I/home/jvogel/site/snakes/py-talk/venv/include/python3.6m -c src/_portaudiomodule.c -o build/temp.linux-x86_64-3.6/src/_portaudiomodule.o
    src/_portaudiomodule.c:29:10: fatal error: portaudio.h: No such file or directory
     #include "portaudio.h"
              ^~~~~~~~~~~~~
    compilation terminated.
    error: command 'x86_64-linux-gnu-gcc' failed with exit status 1
    ----------------------------------------



try installing portaudio dev  

``` sudo apt-get install portaudio19-dev ```
 
