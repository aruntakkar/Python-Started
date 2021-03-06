
# Step 1
# Find total number of lines in the poem

# Step 2
# Print total characters in first and last line

# Step 3
# Find no of times word "I" is used in the poem

# Step 4:
# Replace the last line with
# And that has made all the difference.


def main():
    # poem = """
    # Two roads diverged in a yellow wood,
    # And sorry I could not travel both
    # And be one traveler, long I stood
    # And looked down one as far as I could
    # To where it bent in the undergrowth;
    # Then took the other, as just as fair,
    # And having perhaps the better claim,
    # Because it was grassy and wanted wear;
    # Though as for that the passing there
    # Had worn them really about the same,
    # And both that morning equally lay
    # In leaves no step had trodden black.
    # Oh, I kept the first for another day!
    # Yet knowing how way leads on to way,
    # I doubted if I should ever come back.
    # I shall be telling this with a sigh
    # Somewhere ages and ages hence:
    # Two roads diverged in a wood, and I
    # I took the one less traveled by,
    # And that has made all the difference.
    # """

    poem = """
        Two roads diverged in a yellow wood,
        And sorry I could not travel both
        And be one traveler, long I stood
        And looked down one as far as I could
        To where it bent in the undergrowth;
        Then took the other, as just as fair,
        And having perhaps the better claim,
        Because it was grassy and wanted wear;
        Though as for that the passing there
        Had worn them really about the same,
        And both that morning equally lay
        In leaves no step had trodden black.
        Oh, I kept the first for another day!
        Yet knowing how way leads on to way,
        I doubted if I should ever come back.
        I shall be telling this with a sigh
        Somewhere ages and ages hence:
        Two roads diverged in a wood, and I—
        I took the one less traveled by,
        And that has made all the difference
    """
    # using len and split mehtod
    # method are functions that are part of the particular class

    lines = poem.split('\n')
    print("Total number of lines: {}".format(len(lines)))

    # print("Total number of lines: {}".format(len(lines)))

    # To find the length of each of those lines
    # using the list compression

    # number_of_lines = [len(line) for line in poem.split('\n')]
    # print(number_of_lines)
