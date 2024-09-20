# ComfyUI Exporter

[Prometheus](https://prometheus.io/) exporter for [ComfyUi](https://github.com/comfyanonymous/ComfyUI).

## Installation

### Install from GitHub
1. Install [ComfyUI](https://github.com/comfyanonymous/ComfyUI).
2. Clone this repo into `custom_nodes`:
    ```
    cd ComfyUI/custom_nodes
    git clone https://github.com/aloababa/ComfyUI-Exporter.git
    cd ComfyUI-Exporter
    pip install -r requirements.txt
    ```
3. Start up ComfyUI.

## Metrics output

```
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 3506.0
python_gc_objects_collected_total{generation="1"} 516.0
python_gc_objects_collected_total{generation="2"} 15.0
# HELP python_gc_objects_uncollectable_total Uncollectable objects found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 765.0
python_gc_collections_total{generation="1"} 69.0
python_gc_collections_total{generation="2"} 5.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="10",patchlevel="12",version="3.10.12"} 1.0
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 1.4540222464e+010
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 7.18774272e+08
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1.72685660789e+09
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 14.129999999999999
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 52.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1.048576e+06
# HELP comfyui_queue_remaining Remaining jobs in queue
# TYPE comfyui_queue_remaining gauge
comfyui_queue_remaining 0.0
# HELP comfyui_vram_total Total VRAM
# TYPE comfyui_vram_total gauge
comfyui_vram_total 8.5100068864e+010
# HELP comfyui_vram_free Free VRAM
# TYPE comfyui_vram_free gauge
comfyui_vram_free 4.2587324416e+010
# HELP comfyui_torch_vram_total Total Torch VRAM
# TYPE comfyui_torch_vram_total gauge
comfyui_torch_vram_total 0.0
# HELP comfyui_torch_vram_free Free Torch VRAM
# TYPE comfyui_torch_vram_free gauge
comfyui_torch_vram_free 0.0
```
