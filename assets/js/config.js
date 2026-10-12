/* Site configuration for the Liberty Services prototype.
   heroMode: 'slider' rotates through the four service slides on the home page.
             'static' shows only the first slide (no rotation, no controls).
   The client can also preview either option with ?hero=slider or ?hero=static
   in the URL, or from the "Prototype options" button on the home page.
   heroInterval: milliseconds each slide stays on screen in slider mode.
   showPrototypePanel: set to false before launch to hide the options button. */
window.LIBERTY_CONFIG = {
  heroMode: 'slider',
  heroInterval: 7000,
  showPrototypePanel: true
};
