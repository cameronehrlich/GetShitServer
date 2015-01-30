# GetShitServer
A scraper for Torrentz.eu that presents the user with a list of magnet links.

===

Run:

- ```pip install -r requirements.txt```
- ``` honcho start ```

- ```localhost:5000/search/term+to+search```

--> Returns array of torrents which contain a relative url to a fetch the magnet link with.

- ```localhost:5000/magnet/64dfd9d8a23453ae0cce7847e2ad313b1fad0991```

--> Returns a dictionary containing a magnet link.