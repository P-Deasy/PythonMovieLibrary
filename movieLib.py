from functools import total_ordering

@total_ordering
class Movie:
    """ Represents a single Movie. """

    def __init__(self, i_title, i_date=None, i_runtime=None):
        """ Initialise a Movie Object. """
        self._title = i_title
        self._date = i_date
        self._time = i_runtime

    def __str__(self):
        """ Return a short string representation of this movie. """
        outstr = self._title
        return outstr

    def full_str(self):
        """ Return a full string representation of this movie. """
        outstr = self._title + ": "
        outstr = outstr + str(self._date) + "; "
        outstr = outstr + str(self._time)
        return outstr

    def get_title(self):
        """ Return the title of this movie. """
        return self._title

    def __eq__(self, other):
        """ Return True if this movie has exactly same title as other. """
        if (other._title == self._title):
            return True
        return False

    def __ne__(self, other):
        """ Return False if this movie has exactly same title as other. """
        return not (self._title == other._title)

    def __lt__(self, other):
        """ Return True if this movie is ordered before other.

        A movie is less than another if it's title is alphabetically before.
        """
        if other._title > self._title:
            return True
        return False


from bstStub import BSTNode


class MovieLib:
    """ A movie library.

    Implemented using a BST. 
    """
    
    def __init__(self):
        """ Initialise a movie library. """
        self.bst = BSTNode(None)

    def __str__(self):
        """ Return a string representation of the library.

        The string will be created by an in-order traversal.
        """
        return str(self.bst)

    def size(self):
        """ Return the number of movies in the library. """
        return self.bst.size()

    def search(self, title):
        """ Return Movie with matching title if there, or None.

        Args:
            title: a string representing a movie title.
        """
        return self.bst.search(Movie(title))

    def add(self, title, date, runtime):
        """ Add a new move to the library.

        Args:
            title - the title of the movie
            date - the date the movie was released
            runtime - the running time of the movie

        Returns:
            the movie file that was added, or None
        """
        return self.bst.add(Movie(title, date, runtime))

    def remove(self, title):
        """ Remove and return the a movie object with the given title, if there.

        Args:
            title - the title of the movie to be removed
        """
        return self.bst.remove(Movie(title))

    def _testadd(self):
        library = MovieLib()
        library.add("Memento", "11/10/2000", 113)
        print(str(library))
        print('> adding Melvin and Howard')
        library.add("Melvin and Howard", "19/09/1980", 95)
        print(str(library))
        print('> adding a second version of Melvin and Howard')
        library.add("Melvin and Howard", "21/03/2007", 112)
        print(str(library))
        print('> adding Mellow Mud')
        library.add("Mellow Mud", "21/09/2016", 92)
        print(str(library))
        print('> adding Melody')
        library.add("Melody", "21/03/2007", 113)
        print(str(library))
        return library


def build_library(filename):
    """ Return a library of Movie files built from filename """

    # open the file
    file = open(filename, 'r', encoding="utf8")

    # create the library
    library = MovieLib()

    filecount = 0

    # now cycle through the  lines in the file, adding the movies to the
    # library
    for line in file:
        filecount += 1
        inputlist = line.split('\t')
        library.add(inputlist[0], inputlist[1], inputlist[2])

    # print out some info for sanity checking
    print("read a file with", filecount, "movies")
    return library

