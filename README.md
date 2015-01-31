# Get Shit 
This is a simple Flask app that provides a simple UI and API for a scrapper of Torrentz.eu I am hoping to open source it and add a couple of additional features.  Any help and/or ideas are welcome, but please keep your pull requests consice and simple.

===

-% ```pip install -r requirements.txt```

-% ```honcho start```

-% ```localhost:5000/search/term+to+search```

--> Returns array of torrents which contain a relative url to a fetch the magnet link with.

-% ```localhost:5000/magnet/64dfd9d8a23453ae0cce7847e2ad313b1fad0991```

--> Returns a dictionary containing a magnet link.