cmake_minimum_required(VERSION 3.23)
project(NJU_study C)

set(CMAKE_C_STANDARD 11)

include_directories(.)
include_directories(CLASS2)
include_directories(OSTEP)

add_executable(
        NJU_study
#        CLASS2/alipay.c
#        CLASS2/mem-ordering.c
#        CLASS2/peterson-barrier.c
#        CLASS2/shm-test.c
#        CLASS2/stack-probe.c
#        CLASS2/sum.c
#        CLASS2/thread.h
#        OSTEP/thread26_1.c
        OSTEP/simple_lock.c
#        thread.h

        )
