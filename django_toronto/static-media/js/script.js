// UI behaviours
(function () {
  var App = {
    // Initializes the whole page
    init: function () {
      this.ensureElements();
      this.attachEvents();
    },

    ensureElements: function () {
      this.$homeLogo = $('#home-logo');
      this.$mainLogo = $('#main-logo');
    },

    // Event binding and delegation for all pages
    attachEvents: function () {
      // Adds scrolling animation for internal links
      $('a[href^=#]').on('click', this._scrollToElement);

      // Event for displaying small logo in top bar when main logo is out of viewport
      // Only do this if the main logo is on the page
      if (this.$mainLogo.length) {
        $(window).on('scroll', $.proxy(this._viewportScrollHandler, this));
      }
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
    },

    _viewportScrollHandler: function (e) {
      $('#home-logo').toggleClass('invisible', $('#main-logo').is(':in-viewport'))
      this.$homeLogo.toggleClass('invisible', this.$mainLogo.is(':in-viewport'), 'slow');
    }
  };

  // Wait for DOM ready
  $(function () {
    App.init();
  });
})();
