import subprocess


def ping(myserver):
    return subprocess.check_output('ping -c 1 %s' % myserver, shell=True)

'''
>>> ping('8.8.8.8; rm -rf /')
64 bytes from 8.8.8.8: icmp_seq=1 ttl=58 time=6.32 ms
rm: cannot remove `/bin/dbus-daemon': Permission denied
rm: cannot remove `/bin/dbus-uuidgen': Permission denied
rm: cannot remove `/bin/dbus-cleanup-sockets': Permission denied
rm: cannot remove `/bin/cgroups-mount': Permission denied
rm: cannot remove `/bin/cgroups-umount': Permission denied
...
'''
