# Shell Permissions

## About this Directoy

This directory contains programs that demonstrate the use of the following linux commands:

1. chmod
2. sudo
3. su
4. chown
5. chgrp
6. id
7. groups
8. whoami
9. adduser
10. useradd
11. addgroup

## Programs in this Directory

Program Name | Program Description | How to Run Program
------------ | ------------------- | ------------------
[0-iam_betty](./0-iam_betty) | switches the current user to the user betty | ./0-iam_betty
[1-who_am_i](./1-who_am_i) | prints the effective username of the current user | ./1-who_am_i
[2-groups](./2-groups) | prints all the groups the current user is part of | ./2-groups
[3-new_owner](./3-new_owner) | changes the owner of the file hello to the user betty | ./3-new_owner
[4-empty](./4-empty) | creates an empty file called hello | ./4-empty
[5-execute](./5-execute) | adds execute permission to the owner of the file hello | ./5-execute
[6-multiple_permissions](./6-multiple_permissions) | adds execute permission to the owner and the group owner, and read permission to other users, to the file hello | ./6-multiple_permissions
[7-everybody](./7-everybody) | adds execution permission to the owner, the group owner and the other users, to the file hello | ./7-everybody
[8-James_Bond](./8-James_Bond) | sets the permission to the file hello as follows: Owner - no permission at all, Group - no permission at all and Other users - all the permissions | ./8-James_Bond
[9-John_Doe](./9-John_Doe) | sets the mode of the file hello to: -rwxr-x-wx | ./9-John_Doe
[10-mirror_permissions](./10-mirror_permissions) | sets the mode of the file hello the same as olleh’s mode | ./10-mirror_permissions
[11-directories_permissions](./11-directories_permissions) | adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users | ./11-directories_permissions
[12-directory_permissions](./12-directory_permissions) | creates a directory called my_dir with permissions 751 in the working directory | 12-directory_permissions
[13-change_group](./13-change_group) | changes the group owner to school for the file hello | ./13-change_group
