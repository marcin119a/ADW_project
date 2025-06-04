import numpy as np


class CellCrop:
    """Class representing a single cell crop. """
    
    def __init__(self, cell_id, img, mask, label, slices):
        self.cell_id = cell_id
        self.img = img
        self.mask = mask
        self.label = label
        self.slices = slices

    def sample(self):
        h_slice, w_slice = self.slices

        cropped_image = self.img[:, h_slice, w_slice]
        cropped_mask = self.mask[h_slice, w_slice]

        return {
            'cell_id': self.cell_id,
            'image': cropped_image,
            'mask': (cropped_mask == self.cell_id).astype(np.float16),
            'all_masks': (cropped_mask > 0).astype(np.float16),
            'label': self.label
        }
