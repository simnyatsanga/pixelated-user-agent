/*
 * Copyright (c) 2014 ThoughtWorks, Inc.
 *
 * Pixelated is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * Pixelated is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with Pixelated. If not, see <http://www.gnu.org/licenses/>.
 */
'use strict';
define(['flight/lib/component', 'page/events'], function (defineComponent, events) {

  return defineComponent(function() {

    this.closeSlider = function (){
      $('.exit-off-canvas').click();
    };

    this.after('initialize', function () {
      this.on($('#middle-pane-container'), 'click', this.closeSlider);
      this.on($('#right-pane'), 'click', this.closeSlider);
    });
  });
});
