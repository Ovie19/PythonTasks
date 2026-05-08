def do_this(word):
    for row in range(len(word), 0, -1):
        for column in range(row):
            print(word[column], end=" ")
        print()

do_this("STEP")
do_this("NIGGA")
do_this("NIGGATA")
#
#S T E P
#S T E
#S T
#S