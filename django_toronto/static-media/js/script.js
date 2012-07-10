// UI behaviours
(function () {
  var App = {
    // Initializes the whole page
    init: function () {
      this.initScrolling();
    },

    // Adds scrolling functionality to page anchor links
    initScrolling: function () {
      $('a[href^=#]').on('click', this._scrollToElement);
    },

    _scrollToElement: function (e) {
      e.preventDefault();

      // href would be an anchor link in the page
      var href = e.target.href,
        selector = '#' + href.split('#')[1];
        $div = $(selector);

      $('html,body').animate({
        scrollTop: $div.offset().top
      }, 'slow');
    }
  };

  // Wait for DOM ready
  $(function () {
    App.init();
  });
})();
