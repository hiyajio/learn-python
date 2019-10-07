'''
copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''

def copy(ofile, nfile):
    with open(ofile) as old:
        tocopy = old.read()
    with open(nfile,  "w") as new:
        new.write(tocopy)