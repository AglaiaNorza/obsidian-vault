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

