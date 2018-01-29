import sys

if len(sys.argv) < 2:
    print('usage: python3 update_hosts.py <HOST> <KEY>')
    exit(1)
key = sys.argv[-1]
ip = sys.argv[-2]

lines = []
with open('/etc/hosts') as fp:
    for line in fp.readlines():
        print(line)
        splitted_line = line.split('\t')
        if splitted_line[-1] == key + "\n":
            continue
        lines.append("\t".join(splitted_line))

lines.append("%s\t%s\n" % (ip, key))

with open('/etc/hosts', 'w') as fp:
    for i in lines:
        fp.write(i)

