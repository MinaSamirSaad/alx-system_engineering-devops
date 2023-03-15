# 0x02. Shell, I/O Redirections and filters

## About this Directoy

This directory contains programs that demonstrate make use of the following linux commands.

1. echo
2. cat
3. head
4. tail
5. find
6. wc
7. sort
8. uniq
9. grep
10. tr
11. rev
12. cut
13. passwd (5) (i.e. man 5 passwd)

## Programs in this Directory

Program Name | Program Description | How to Run Program
------------ | ------------------- | ------------------
[0-hello_world](./0-hello_world) | prints “Hello, World”, followed by a new line to the standard output | ./0-hello_world
[1-confused_smiley](./1-confused_smiley) | displays a confused smiley "(Ôo)' | ./1-confused_smiley
[2-hellofile](./2-hellofile) | displays the content of the /etc/passwd file. | ./2-hellofile
[3-twofiles](./3-twofiles) | displays the content of /etc/passwd and /etc/hosts | ./3-twofiles
[4-lastlines](./4-lastlines) | displays the last 10 lines of /etc/passwd | ./4-lastlines
[5-firstlines](./5-firstlines) | displays the first 10 lines of /etc/passwd | ./5-firstlines
[6-third_line](./6-third_line) | displays the third line of the file iacta | ./6-third_line
[7-file](./7-file) | creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line | ./7-file
[8-cwd_state ](./8-cwd_state ) | writes into the file ls_cwd_content the result of the command ls -la | ./8-cwd_state 
[9-duplicate_last_line](./9-duplicate_last_line) | duplicates the last line of the file iacta | ./9-duplicate_last_line 
[10-no_more_js](./10-no_more_js) | deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders | ./10-no_more_js
[11-directories](./11-directories) | counts the number of directories and sub-directories in the current directory | ./11-directories
[12-newest_files](./12-newest_files) | displays the 10 newest files in the current directory | ./12-newest_files
[13-unique](./13-unique) | takes a list of words as input and prints only words that appear exactly once | ./13-unique
[14-findthatword](./14-findthatword) | displays lines containing the pattern “root” from the file /etc/passwd | ./14-findthatword
[15-countthatword](./15-countthatword) | displays the number of lines that contain the pattern “bin” in the file /etc/passwd | ./15-countthatword
[16-whatsnext](./16-whatsnext) | displays lines containing the pattern “root” and 3 lines after them in the file /etc/passwd | ./16-whatsnext
[17-hidethisword](./17-hidethisword) | displays all the lines in the file /etc/passwd that do not contain the pattern “bin” | ./17-hidethisword
[18-letteronly](./18-letteronly) | displays all lines of the file /etc/ssh/sshd_config starting with a letter | ./18-letteronly
[19-AZ ](./19-AZ ) | replaces all characters A and c from input to Z and e respectively | ./19-AZ 
[20-hiago](./20-hiago) | removes all letters c and C from input | ./20-hiago
[21-reverse](./21-reverse) | reverse its input | ./21-reverse
[22-users_and_homes](./22-users_and_homes) | displays all users and their home directories, sorted by users | ./22-users_and_homes
