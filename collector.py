from aiohttp import web
from server import PromptServer
import comfy.model_management
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily, REGISTRY

class PrometheusCollector:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {}

    RETURN_TYPES = ()
    FUNCTION = ""
    OUTPUT_NODE = False
    CATEGORY = ""

    def collect(self):
        device = comfy.model_management.get_torch_device()
        device_name = comfy.model_management.get_torch_device_name(device)

        vram_total_value, torch_vram_total_value = comfy.model_management.get_total_memory(device, torch_total_too=True)
        yield GaugeMetricFamily('comfyui_vram_total', 'Total VRAM', value=vram_total_value)
        yield GaugeMetricFamily('comfyui_torch_vram_total', 'Total Torch VRAM', value=torch_vram_total_value)

        vram_free_value, torch_vram_free_value = comfy.model_management.get_free_memory(device, torch_free_too=True)
        yield GaugeMetricFamily('comfyui_vram_free', 'Free VRAM', value=vram_free_value)
        yield GaugeMetricFamily('comfyui_torch_vram_free', 'Free Torch VRAM', value=torch_vram_free_value)

        queue_info = PromptServer.instance.get_queue_info()
        yield GaugeMetricFamily('comfyui_queue_remaining', 'Remaining jobs in queue', value=queue_info["exec_info"]["queue_remaining"])


@PromptServer.instance.routes.get("/metrics")
async def get_metrics(request):
    response = web.Response(body=generate_latest())
    response.content_type = CONTENT_TYPE_LATEST
    return response

collector = PrometheusCollector()

NODE_CLASS_MAPPINGS = {
    "PrometheusCollector": collector
}

REGISTRY.register(collector)
