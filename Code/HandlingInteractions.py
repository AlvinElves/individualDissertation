from mpl_interactions import panhandler
import matplotlib.pyplot as plt


class HandlingInteractions:
    """
    HandlingInteractions Class to be imported into fils that allows the user to pan and zoom using a mouse.
    """
    @staticmethod
    def zoom_factory(ax, base_scale=2.):
        """
        A function that can be called to matplotlib figure to allow the user to zoom in and out using a mouse.
        :param ax: The subplot axes from the matplotlib figure. This axes allows the user to plot on it
        :param base_scale: How much zooming the user wants each ticks
        :return: The zoom_fun function to allow zooming for the matplotlib figure
        """
        def zoom_fun(event):
            """
            A function that do the calculation of zooming in and out and change the view.
            :param event: The position of the user's mouse arrow for calculation
            :return: Redraw the matplotlib figure based on the user's zoom
            """
            # get the current x and y limits
            cur_xlim = ax.get_xlim()
            cur_ylim = ax.get_ylim()
            cur_xrange = (cur_xlim[1] - cur_xlim[0]) * .5
            cur_yrange = (cur_ylim[1] - cur_ylim[0]) * .5
            xdata = event.xdata  # get event x location
            ydata = event.ydata  # get event y location
            if event.button == 'up':
                # deal with zoom in
                scale_factor = 1 / base_scale
            elif event.button == 'down':
                # deal with zoom out
                scale_factor = base_scale
            else:
                # deal with something that should never happen
                scale_factor = 1

            # set new limits
            ax.set_xlim([xdata - cur_xrange * scale_factor,
                         xdata + cur_xrange * scale_factor])
            ax.set_ylim([ydata - cur_yrange * scale_factor,
                         ydata + cur_yrange * scale_factor])
            plt.draw()  # force re-draw

        fig = ax.get_figure()  # get the figure of interest
        # attach the call back
        fig.canvas.mpl_connect('scroll_event', zoom_fun)

        # return the function
        return zoom_fun