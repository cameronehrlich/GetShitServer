# GetShitServer
A scraper for Torrentz.eu that presents the user with a list of magnet links.

===

Run:

- ```pip install -r requirements```
- ``` honcho start ```


Go to:

- ```localhost:5000/search/term+to+search```

[{
	"date_exact":
	"Wed, 21 Jan 2015 05:56:03",
	"date_relative":
	"7 days",
	"name":
	"State Of The Union 2015 01 20 U S A HDTV x264 mp4",
	"rel_url":
	"4a2dfb2b783aa66026778319da4bf7b10c3b837c",
	"seeders":
	"26",
	"size":
	"447 MB"
},
{
	"date_exact":
	"Mon, 25 Mar 2013 12:40:42",
	"date_relative":
	" 1 year",
	"name":
	"xXx 2 State Of Union 2005 1080p Bluray x264 Dual Audio English Hindi TBI",
	"rel_url":
	"64dfd9d8a23453ae0cce7847e2ad313b1fad0991",
	"seeders":
	"12",
	"size":
	"1644 MB"
}]

- ```localhost:5000/magnet/64dfd9d8a23453ae0cce7847e2ad313b1fad0991```

{
	"magnet":"magnet:?xt=urn:btih:4A2DFB2B783AA66026778319DA4BF7B10C3B837C&dn=state+of+the+union+2015+01+20+u+s+a+hdtv+x264+mp4&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Fopen.demonii.com%3A1337"
}