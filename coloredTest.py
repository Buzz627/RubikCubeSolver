from colored import fg, bg, attr

def colored(text, color):
	return '{}{}{}'.format(fg(color), text, attr(0))

print colored('Hello World', "#FFFF00")
print "foo"

