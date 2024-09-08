### images
the `<img>` element s a void element -it cannot have any child content and cannot have an end tag.
(other than the [[basics#images|other attributes]])
- the `width` and `height` attributes specify an image's width and height
- the `title` attribute provides further information if needed (and is displayed on mouse hover) - but it's not really recommended to use it
- `figure` and `figcaption` are created to provide a semantic container for figures and to clearly link the figure to the caption
 ```html
	<figure>
  <img
    src="images/dinosaur.jpg"
    alt="The head and torso of a dinosaur skeleton;
            it has a large head with long sharp teeth"
    width="400"
    height="341" />
    
  <figcaption>
    A T-Rex on display in the Manchester University Museum.
  </figcaption>
</figure>
```

there are other ways to create and manipulate images with HTML, such as:
- the `<canvas>` element - it provides APIs to draw 2D graphics w/JavaScript
- SVG 
- WebGL (graphics API)

### video and audio
The `video` element allows the embedding of videos.
it has the `src` attribute, and a `controls` keyword (other than the default controls, custom ones can be created with JavaScript)
```html
<video src="video.mp4" controls/>
```

- https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Video_and_audio_content (i do not want to take notes on this rn)

**other < video> features**
```html
<video
  controls
  width="400"
  height="400"
  autoplay
  loop
  muted
  preload="auto"
  poster="poster.png">
  <source src="rabbit320.mp4" type="video/mp4" />
  <source src="rabbit320.webm" type="video/webm" />
  <p>
    Your browser doesn't support this video. Here is a
    <a href="rabbit320.mp4">link to the video</a> instead.
  </p>
</video>
```

The `<audio>` element works like the `<video>` element with a few differences
```html
<audio controls>
  <source src="viper.mp3" type="audio/mp3" />
  <source src="viper.ogg" type="audio/ogg" />
  <p>
    Your browser doesn't support this audio file. Here is a
    <a href="viper.mp3">link to the audio</a> instead.
  </p>
</audio>
```
it supports the same features `<video>` does, except `width`, `height`, and `poster`.

### iframe, embed, object
`<iframe>` elements are designed to embed other web documents into the current document (videos, maps etc).
The bare essentials needed for an `<iframe>` are:
- `border: none`
- `allowfullscreen
- `src`
- `width`, `height`
- `sandbox` - content that's not sandboxed may be able to execute JavaScript, submit forms, trigger popup windows, etc.

The `<embed>` and `<object>` elements are general purpose embedding tools for external content (like pdfs).

### vector graphics
SVG is a XML-based language for describing vector images.
It defines elements for creating basic and complex shapes.

SVGs can be embedded via an `<img>` element like a normal image, or the SVG code can be pasted inside an HTML document (*inlining SVG*) with `<svg></svg>`. Another way to embed SVGs is through `iframe`, but it's not recommended.

### responsive images
Sometimes the need to display images with varying sizes arises - this can be fixed with the `srcset` and `sizes` attributes.
- `srcset` defines the set of images the browser can choose between, and what size each image is. Each set of image information is separated from the others by a comma. The syntax is:
	1) image filename
	2) space
	3) image's intrinsic width in pixels (not `px`)
- `sizes` defines a set of media conditions (like screen widths) and indicates what image size would be the best choice. The syntax is:
	1) a media condition (ex `max-width:600px`)
	2) space
	3) the width of the slot the image will fill when the media condition is true

With these attributes in place, the browser will:

- Look at screen size, pixel density, zoom level, screen orientation, and network speed.
- Work out which media condition in the sizes list is the *first one to be true*.
- Look at the slot size given to that media query.
- Load the image referenced in the srcset list that has the same size as the slot or, if there isn't one, the first image that is bigger than the chosen slot size.

For resolution issues, the browser can choose an appropriate resolution image with the use of `srcset` with x-descriptors (1.5x, 2x) and without sizes.
```html
<img
  srcset="elva-fairy-320w.jpg, elva-fairy-480w.jpg 1.5x, elva-fairy-640w.jpg 2x"
  src="elva-fairy-640w.jpg"
  alt="Elva dressed as a fairy" />
```

The `<picture>` element allows us to implement the changing of sizes. It contains multiple `<source>` elements that provide different sources for the browser to choose from, followed by the `<img>` element.
```html
<picture>
  <source media="(max-width: 799px)" srcset="elva-480w-close-portrait.jpg" />
  <source media="(min-width: 800px)" srcset="elva-800w.jpg" />
  <img src="elva-800w.jpg" alt="Chris standing up holding his daughter Elva" />
</picture>
```