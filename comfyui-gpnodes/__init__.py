from .if_else import IfElse, MatchTextToInput
from .latent_resolution_selector import LatentResolutionSelector
from .resize_image import ResizeImage
from .free_vram_model import FreeVRAM, PurgeCLIPNode



#  Map all your custom nodes classes with the names that will be displayed in the UI.
NODE_CLASS_MAPPINGS = {
    "GPNodes_IfElse": IfElse,
    "GPNodes_ResizeImage": ResizeImage,
    "GPNodes_LatentResolutionSelector": LatentResolutionSelector,
    "GPNodes_FreeVRAM": FreeVRAM,
    "GPNodes_PurgeCLIPNode": PurgeCLIPNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GPNodes_IfElse": "🔀 If-Else (input / compare_with)",
    "GPNodes_ResizeImage": "📏 Resize Image",
    "GPNodes_LatentResolutionSelector": "🖼 Empty Latent Selector",
    "GPNodes_FreeVRAM": "🧹➜🖥 Free VRAM",
    "GPNodes_PurgeCLIPNode": "🧹➜🖼 Purge CLIP Node"
}

__all__ = ['NODE_CLASS_MAPPINGS','NODE_DISPLAY_NAME_MAPPINGS']
