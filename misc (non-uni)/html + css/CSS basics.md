![[css-declaration-small.png]]

important rules:
- each ruleset must be wrapped in curly braces
- within each declaration, a colon must be used to separate the property from its value(s)
- within each ruleset, a semicolon is needed to separate each declaration from the next one

```CSS
p {
  color: red;
  width: 500px;
  border: 1px solid black;
}
```

### element selectors
- element selectors select all of the elements of  one type
- class selectors (which start with a `.` in CSS) (in the html tag) only target elements belonging to that class
- id selectors (in the html tag) should be unique (not used more than once) but they shouldn't really be used in CSS\
- the universal selector `*` selects everything - but it's mainly used for a CSS reset

selectors can be **grouped** with a comma:
```css
h1, h2 {
	color: blue;
}
```

instead, `h1 h2` looks for an h2 that is nested inside an h1.

> [!info] CSS is a cascading-style language, so the _last_ rule is the one that applies (but *specificity* overrides order).

>[!info] inheritance
>In CSS, if a rule is set for a parent class, all of the classes that derive from it will inherit it. But typically, only things related to typography are inhereted.

### colors
colors can be set with:
- color names (140 available)
- RGB - `color: rgb(0,0,0)`
- RGBA  (the *alpha* property adds transparency, with 1=fully opaque)
- hex
- hsl

colors can be set with:
- `background-color:` / `background:`
- `color:` (font-color)

### units
units determine the sizes of everything in a page.
the most popular ones are: 
- `px` (absolute unit, not recommended for font sizes since it's not affected by the browser settings - better for things like `border`) 
- `percentage` (not ideal for fonts either, better for elements ) - relative to the parent
- `rem` (typically used for font size) - relative to the size of the root element (by default, most browsers use a font size value of 16px. so, if the root element is 16px, an element with the value 1rem will also equal 16px)
```CSS
p {
	font-size: 2rem; /* typically 32px (16*2) /
}
```
- `em` depends on the font-size of the parent element - it could be used in something like this:
```CSS
h1 {
	font-size: 3rem;
	padding: 1em;
}
/* here, 1em is equivalent to the 3em font-size (because the element's size is 3em) /
```

- `ch` - the width of the glyph "0" of the element's font (helps to set the character width) - for example, one could give a paragraph a width of 40ch to make it span around 40 characters:
```CSS
p {
	font-size: 2rem;
	width: 40ch;
}
```

> [!warning] css reset
>```
> * {
> 	margin: 0;
> 	padding: 0;
> 	box-sizing: border-box;
> } 
>```
>this overrides the default values set by (the browser?)
>

- `vw` - relative to  the viewport width 

### box models
![[boxmodel.png]]

a basic CSS reset's goal is to reset settings like margin, paddings etc
```CSS
* {
	  margin: 0;
	  padding: 0;
	  box-sizing: content-box;:
  }
```

another box-sizing option is: `border-box`. `border-box` calculates the dimensions based on a sum of the contents of the border:
(it includes the border and the padding, but not the margin)
```CSS
h1 {
	border: 2px dashed red;
	width: 400px;
	padding: 0.5em;
}
*/ in this case, the content would be 348px, plus the 24 px of padding and 2px of border *
```
