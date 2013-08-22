americanarchivist
=================

This is a crawler that *slowly* walks through issues of the [American Archivist](http://archivists.metapress.com/content/120809) and records metadata for each article as JSON that will look something like this:

```javascript
{
  "volume": "76",
  "issue": "1", 
  "title": "Like a Box of Chocolates: A Case Study of User-Contributed Content at Footnote", 
  "author": [
    {
      "name": "Pamela H. Mayer", 
      "organization": "University of North Carolina at Chapel Hill"
    }
  ], 
  "pdf": "http://archivists.metapress.com/content/up5u15p2k1826686/fulltext.pdf?page=1", 
  "image": "http://resources.metapress.com/pdf-preview.axd?code=up5u15p2k1826686&size=largest", 
  "pages": "19-46", 
  "url": "http://archivists.metapress.com/content/up5u15p2k1826686/?p=84d659b4d23a4dc2b2d2dbbf391570f2&pi=2", 
  "abstract": "User-contributed content has been suggested as a means to narrow the gap between the level of description that resource-constrained repositories are able to provide and the level of description that users need or have come to expect. Research seems to indicate that allowing users to contribute content holds some promise for augmenting traditional description, thus increasing the discoverability of materials. As yet, the practice of allowing user-contributed content has not been widely adopted, especially for large-scale online collections. Because this is not an endeavor to be entered into lightly in terms of required resources or policy considerations, it is important for decision makers to have as much information as possible about who will contribute content and what that content looks like. It is informative to look at the experience of Footnote, an entity with an existing online collection with user contribution functionality. This case study identifies individuals with family connections to a collection as the largest group of contributors, while annotations are the most common type of contribution. The data suggest that users are predominately interested in information about individuals. This study also indicates that there are issues of consistency, authenticity, and context with regard to user-contributed content."
}
```

Running
-------

If you want to run `crawl.py` you will need [Python](http://python.org) and 
also to install the dependencies found in `requirements.txt`
