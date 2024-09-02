### elements
HTML consists of a series of **elements** which can be used to enclose different parts of the content to make it appear a certain way, or act a certain way.
The elements can be recognised thanks to **tags** --> the element's name surrounded by <> (element names are case-insensitive).

![[html elements.png]]

elements can also have **attributes**:
![[attributes.png]]

and elements can be **nested**:

```html
<p>My cat is extremely <strong>cute</strong>.</p>
```
#### void elements
void elements are elements that have no content.

```html
<img src="images/firefox-icon.png" alt="My test image" />
```

an image element doesn't wrap content to affect it, so it doesn't have a closing tag or any inner content.

### pages

```html
<!doctype html>
<html lang="en-US">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <title>My test page</title>
  </head>
  <body>
    <img src="images/firefox-icon.png" alt="My test image" />
  </body>
</html>
```

- `<!doctype html>` is a required element
- `<html></html>` wraps the content on the entire page - it's a *root element* and it sets the language of the document
- `<head></head>` acts as a container for the things that **won't be shown** on the page (keywords, a page description, CSS etc)
- `<meta charset="utf-8" />` the character set should use utf-8
- `<meta name="viewport" content="width=device-width" />` (the mobile browser's *viewport* is the area of the window in which web content can be seen, which is not necessarily the same size as the rendered page.)  - this element ensures the page renders at the width of the viewport.
- `<title></title>` title of the page - appears in the browser tab the page is loaded in
```
- `<body></body>` contains **all the content that is shown**
```

## main elements
(comments are written inside `<!--` `-->`)
#### headings
HTML contains 6 heading levels (1-6)

#### images
The `<img>` element contains: 
- a `src` attribute - the path to the image
- a `alt` attribute - a description of the image (used for visually impaired people or for when the image doesn't load)

