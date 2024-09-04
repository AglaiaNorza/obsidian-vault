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

