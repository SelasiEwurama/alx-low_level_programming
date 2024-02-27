# 0x1C. C - Makefiles

## Tasks
### 0. make -f 0-Makefile
Create your first Makefile.
<ul>
<li>name of the executable: school</li>
<li>rules: all<ul><li>The all rule builds your executable</li></ul></li>
<li>variables: none</ul>
</ul>

<pre>
<code>
```
julien@ubuntu:~/0x1C. Makefiles$ make -f 0-Makefile 
gcc main.c school.c -o school
julien@ubuntu:~/0x1C. Makefiles$ ./school 
j#0000000000000000000000000000000000000
j#000000000000000000@Q**g00000000000000
j#0000000000000000*]++]4000000000000000
j#000000000000000k]++]++*N#000000000000
j#0000000000000*C+++]++]++]J*0000000000
j#00000000000@+]++qwwwp=]++++]*00000000
j#0000000000*+++]q#0000k+]+]++]4#000000
j#00000000*C+]+]w#0000*]+++]+]++0000000
j#0000we+]wW000***C++]++]+]++++40000000
j#000000000*C+]+]]+]++]++]++]+q#0000000
j#0000000*]+]+++++++]++]+++]+++J0000000
j#000000C++]=]+]+]+]++]++]+]+]+]=000000
j#00000k+]++]+++]+]++qwW0000000AgW00000
j#00000k++]++]+]+++qW#00000000000000000
j#00000A]++]++]++]++J**0000000000000000
j#000000e]++]+++]++]++]J000000000000000
j#0000000A]++]+]++]++]++000000000000000
j#000000000w]++]+]++]+qW#00000000000000
j#00000000000w]++++]*0##000000000000000
j#0000000000000Ag]+]++*0000000000000000
j#00000000000000000we]+]Q00000000000000
j#0000000000000@@+wgdA]+J00000000000000
j#0000000000000k?qwgdC=]4#0000000000000
j#00000000000000w]+]++qw#00000000000000
"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
julien@ubuntu:~/0x1C. Makefiles$
```
</code>
</pre>


### 1. make -f 1-Makefile
Requirements:
<ul>
<li>name of the executable: school</li>
<li>rules: all <ul><li>The all rule builds your executable</li></ul></li>
<li>variables: CC, SRC <ul><li>CC: the compiler to be used</li><li>SRC: the .c files</li></ul></li>
</ul>

<pre>
<code>
julien@ubuntu:~/0x1C. Makefiles$ make -f 1-Makefile
gcc main.c school.c -o school
julien@ubuntu:~/0x1C. Makefiles$ make -f 1-Makefile
gcc main.c school.c -o school
julien@ubuntu:~/0x1C. Makefiles$
</code>
</pre>

 
### 2. make -f 2-Makefile
Create your first useful Makefile.
Requirements:
<ul>
<li>name of the executable: school</li>
<li>rules: all <ul><li>The all rule builds your executable</li></ul></li>
<li>variables: CC, SRC, OBJ, NAME
<ul><li>CC: the compiler to be used</li>
<li>SRC: the .c files</li>
<li>OBJ: the .o files</li>
<li>NAME: the name of the executable</li></ul>
<li>The all rule should recompile only the updated source files</li>
<li>You are not allowed to have a list of all the .o files</li>
</ul>

<pre>
<code>
julien@ubuntu:~/0x1C. Makefiles$ make -f 2-Makefile
gcc    -c -o main.o main.c
gcc    -c -o school.o school.c
gcc main.o school.o -o school
julien@ubuntu:~/0x1C. Makefiles$ make -f 2-Makefile
gcc main.o school.o -o school
julien@ubuntu:~/0x1C. Makefiles$ echo "/* School */" >> main.c
julien@ubuntu:~/0x1C. Makefiles$ make -f 2-Makefile
gcc    -c -o main.o main.c
gcc main.o school.o -o school
julien@ubuntu:~/0x1C. Makefiles$
</code>
</pre>


### 3. make -f 3-Makefile
Requirements:
<ul>
<li>name of the executable: school</li>
<li>rules: all, clean, oclean, fclean, re
<ul><li>all: builds your executable</li>
<li>clean: deletes all Emacs and Vim temporary files along with the executable</li>
<li>oclean: deletes the object files</li>
<li>fclean: deletes all Emacs and Vim temporary files, the executable, and the object files</li>
<li>re: forces recompilation of all source files</li></ul></li>
<li>variables: CC, SRC, OBJ, NAME, RM
<ul><li>CC: the compiler to be used</li>
<li>SRC: the .c files</li>
<li>OBJ: the .o files</li>
<li>NAME: the name of the executable</li>
<li>RM: the program to delete files</li></ul></li>
<li>The all rule should recompile only the updated source files</li>
<li>The clean, oclean, fclean, re rules should never fail</li>
<li>You are not allowed to have a list of all the .o files</li>
</ul>

<pre>
<code>
julien@ubuntu:~//0x1C. Makefiles$ ls -1
0-Makefile
1-Makefile
2-Makefile
3-Makefile
school.c
main.c
main.c~
m.h
julien@ubuntu:~/0x1C. Makefiles$ make -f 3-Makefile
gcc    -c -o main.o main.c
gcc    -c -o school.o school.c
gcc main.o school.o -o school
julien@ubuntu:~/0x1C. Makefiles$ make all -f 3-Makefile
gcc main.o school.o -o school
julien@ubuntu:~/0x1C. Makefiles$ ls -1
0-Makefile
1-Makefile
2-Makefile
3-Makefile
school
school.c
school.o
main.c
main.c~
main.o
m.h
julien@ubuntu:~/0x1C. Makefiles$ make clean -f 3-Makefile 
rm -f *~ school
julien@ubuntu:~/0x1C. Makefiles$ make oclean -f 3-Makefile 
rm -f main.o school.o
julien@ubuntu:~/0x1C. Makefiles$ make fclean -f 3-Makefile 
rm -f *~ school
rm -f main.o school.o
julien@ubuntu:~/0x1C. Makefiles$ make all -f 3-Makefile
gcc    -c -o main.o main.c
gcc    -c -o school.o school.c
gcc main.o school.o -o school
julien@ubuntu:~/0x1C. Makefiles$ make all -f 3-Makefile
gcc main.o school.o -o school
julien@ubuntu:~/0x1C. Makefiles$ make re -f 3-Makefile
rm -f main.o school.o
gcc    -c -o main.o main.c
gcc    -c -o school.o school.c
gcc main.o school.o -o school
julien@ubuntu:~/0x1C. Makefiles$
</code></pre>


### 4. A complete Makefile
Requirements:
<ul>
<li>name of the executable: school</li>
<li>rules: all, clean, fclean, oclean, re
<ul><li>all: builds your executable</li>
<li>clean: deletes all Emacs and Vim temporary files along with the executable</li>
<li>oclean: deletes the object files</li>
<li>fclean: deletes all Emacs and Vim temporary files, the executable, and the object files</li>
<li>re: forces recompilation of all source files</li></ul></li>
<li>variables: CC, SRC, OBJ, NAME, RM, CFLAGS
<ul></li>CC: the compiler to be used</li>
<li>SRC: the .c files</li>
<li>OBJ: the .o files</li>
<li>NAME: the name of the executable</li>
<li>RM: the program to delete files</li>
<li>CFLAGS: your favorite compiler flags: -Wall -Werror -Wextra -pedantic</li>
</ul></li>
<li>The all rule should recompile only the updated source files</li>
<li>The clean, oclean, fclean, re rules should never fail</li>
<li>You are not allowed to have a list of all the .o file</li>
</ul>

<pre><code>
julien@ubuntu:~/0x1C. Makefiles$ make all -f 4-Makefile
gcc -Wall -Werror -Wextra -pedantic   -c -o main.o main.c
gcc -Wall -Werror -Wextra -pedantic   -c -o school.o school.c
gcc main.o school.o -o school
julien@ubuntu:~/0x1C. Makefiles$
</code></pre>


### 5. Island Perimeter
Technical interview preparation:
<ul>
<li>You are not allowed to google anything</li>
<li>Whiteboard first</li>
</ul>

Create a function def island_perimeter(grid): that returns the perimeter of the island described in grid:
<ul>
<li>grid is a list of list of integers:
<ul><li>0 represents a water zone</li>
<li>1 represents a land zone</li>
<li>One cell is a square with side length 1</li>
<li>Grid cells are connected horizontally/vertically (not diagonally).</li>
<li>Grid is rectangular, width and height don’t exceed 100</li></ul></li>
<li>Grid is completely surrounded by water, and there is one island (or nothing).</li>
<li>The island doesn’t have “lakes” (water inside that isn’t connected to the water around the island).</li>
</ul>

Requirements:
<ul>
<li>First line contains #!/usr/bin/python3</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>
guillaume@ubuntu:~/0x1C$ cat 5-main.py
#!/usr/bin/python3
"""
5-main
"""
island_perimeter = __import__('5-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

guillaume@ubuntu:~/0x1C$ 
guillaume@ubuntu:~/0x1C$ ./5-main.py
12
guillaume@ubuntu:~/0x1C$
</code></pre>

## Advanced Tasks

### 6. make -f 100-Makefile
Requirements:
<ul>
<li>name of the executable: school</li>
<li>rules: all, clean, fclean, oclean, re
<ul><li>all: builds your executable</li>
<li>clean: deletes all Emacs and Vim temporary files along with the executable</li>
<li>oclean: deletes the object files</li>
<li>fclean: deletes all Emacs and Vim temporary files, the executable, and the object files</li>
<li>re: forces recompilation of all source files</li></ul></li>
<li>variables: CC, SRC, OBJ, NAME, RM, CFLAGS
<ul><li>CC: the compiler to be used</li>
<li>SRC: the .c files</li>
<li>OBJ: the .o files</li>
<li>NAME: the name of the executable</li>
<li>RM: the program to delete files</li>
<li>CFLAGS: your favorite compiler flags: -Wall -Werror -Wextra -pedantic</li></ul></li>
<li>The all rule should recompile only the updated source files</li>
<li>The clean, oclean, fclean, re rules should never fail</li>
<li>You are not allowed to have a list of all the .o files</li>
<li>You have to use $(RM) for the cleaning up rules, but you are not allowed to set the RM variable</li>
<li>You are not allowed to use the string $(CC) more than once in your Makefile</li>
<li>You are only allowed to use the string $(RM) twice in your Makefile</li>
<li>You are not allowed to use the string $(CFLAGS) (but the compiler should still use the flags you set in this variable)</li>
<li>You are not allowed to have an $(OBJ) rule</li>
<li>You are not allowed to use the %.o: %.c rule</li>
<li>Your Makefile should work even if there is a file in the folder that has the same name as one of your rule</li>
<li>Your Makefile should not compile if the header file m.h is missing</li>
</ul>

