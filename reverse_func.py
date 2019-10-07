'''
copy_and_reverse('story.txt', 'story_reversed.txt') # None
# expect the contents of story_reversed.txt to be the reverse of the contents of story.txt
'''

def copy_and_reverse(ofile, nfile):
    with open(ofile) as old:
        tocopy = old.read()
    with open(nfile,  "w") as new:
        new.write(tocopy[::-1])