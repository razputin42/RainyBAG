from PyQt5.QtWidgets import QTabBar


class TabBar(QTabBar):
    def sizeHint(self):
        hint = super().sizeHint()
        if self.isVisible() and self.parent():
            if not self.shape() & self.RoundedEast:
                # horizontal
                hint.setWidth(self.parent().width())
            else:
                # vertical
                hint.setHeight(self.parent().height())
        return hint

    def tabSizeHint(self, index):
        hint = super().tabSizeHint(index)
        if not self.shape() & self.RoundedEast:
            averageSize = self.width() / self.count()
            if super().sizeHint().width() < self.width() and hint.width() < averageSize:
                hint.setWidth(averageSize)
        else:
            averageSize = self.height() / self.count()
            if super().sizeHint().height() < self.height() and hint.height() < averageSize:
                hint.setHeight(averageSize)
        return hint