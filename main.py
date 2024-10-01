import timeit
import multiprocessing
import numpy as np
import time
import threading
import zlib
import os  # 导入 os 模块以便删除文件

# 基准时间，用于标准化得分
BASELINE_SINGLE_CORE = 5.0  # 假设单核基准时间为 5 秒
BASELINE_MULTI_CORE = 2.5  # 假设多核基准时间为 2.5 秒
BASELINE_MATRIX = 10.0  # 矩阵乘法基准时间为 10 秒
BASELINE_MEMORY = 3.0  # 内存操作基准时间为 3 秒
BASELINE_FLOAT = 4.0  # 浮点运算基准时间为 4 秒
BASELINE_INTEGER = 3.0  # 整数计算基准时间为 3 秒
BASELINE_THREAD_SWITCH = 0.2  # 线程切换基准时间为 0.2 秒
BASELINE_SORT = 2.0  # 排序基准时间为 2 秒
BASELINE_COMPRESS = 2.0  # 压缩解压缩基准时间为 2 秒
BASELINE_IO = 5.0  # 文件 I/O 基准时间为 5 秒


# 单核性能测试
def single_core_test():
    def test_function():
        total = 0
        for i in range(10000000):
            total += i
        return total

    execution_time = timeit.timeit(test_function, number=5)
    score = BASELINE_SINGLE_CORE / execution_time * 100  # 标准化得分
    return execution_time, score


# 多核性能测试
def test_function(_):
    total = 0
    for i in range(10000000):
        total += i
    return total


def multi_core_test():
    num_cores = multiprocessing.cpu_count()  # 获取 CPU 核心数
    start_time = time.time()

    # 使用进程池运行多核测试
    with multiprocessing.Pool(processes=num_cores) as pool:
        pool.map(test_function, range(num_cores))  # 传递 range(num_cores) 作为参数

    end_time = time.time()
    execution_time = end_time - start_time
    score = BASELINE_MULTI_CORE / execution_time * 100  # 标准化得分
    return execution_time, score


# 矩阵计算性能测试
def matrix_test():
    matrix_size = 3000
    A = np.random.rand(matrix_size, matrix_size)
    B = np.random.rand(matrix_size, matrix_size)

    start_time = time.time()
    C = np.dot(A, B)
    end_time = time.time()
    execution_time = end_time - start_time
    score = BASELINE_MATRIX / execution_time * 100  # 标准化得分
    return execution_time, score


# 内存带宽测试
def memory_bandwidth_test():
    array_size = 100000000  # 1亿个元素
    A = np.random.rand(array_size)

    start_time = time.time()
    B = A * 2
    end_time = time.time()
    execution_time = end_time - start_time
    score = BASELINE_MEMORY / execution_time * 100  # 标准化得分
    return execution_time, score


# 浮点运算性能测试
def floating_point_test():
    array_size = 10000000  # 1000万个元素
    A = np.random.rand(array_size)

    start_time = time.time()
    B = np.sin(A) + np.cos(A)  # 浮点运算
    end_time = time.time()
    execution_time = end_time - start_time
    score = BASELINE_FLOAT / execution_time * 100  # 标准化得分
    return execution_time, score


# 整数计算性能测试
def integer_calculation_test():
    def test_function():
        total = 1
        for i in range(1, 10000000):
            total *= i
            if total > 1e12:
                total = 1
        return total

    execution_time = timeit.timeit(test_function, number=5)
    score = BASELINE_INTEGER / execution_time * 100
    return execution_time, score


# 线程切换性能测试
def thread_switching_test():
    def worker():
        for _ in range(100000):
            pass

    start_time = time.time()

    # 创建和启动多个线程
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=worker)
        thread.start()
        threads.append(thread)

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    end_time = time.time()
    execution_time = end_time - start_time
    score = BASELINE_THREAD_SWITCH / execution_time * 100
    return execution_time, score


# 排序算法性能测试
def sorting_test():
    array_size = 1000000
    A = np.random.rand(array_size)

    start_time = time.time()
    sorted_A = np.sort(A)
    end_time = time.time()
    execution_time = end_time - start_time
    score = BASELINE_SORT / execution_time * 100
    return execution_time, score


# 压缩解压缩性能测试
def compression_test():
    data = b"A" * 10000000  # 生成 1000 万字节的数据

    start_time = time.time()
    compressed_data = zlib.compress(data)
    decompressed_data = zlib.decompress(compressed_data)
    end_time = time.time()

    execution_time = end_time - start_time
    score = BASELINE_COMPRESS / execution_time * 100
    return execution_time, score


# 文件 I/O 性能测试
def file_io_test():
    file_size = 100000000  # 100MB
    data = b"A" * file_size
    file_name = "test_file_io.tmp"

    # 写入文件
    start_time = time.time()
    with open(file_name, "wb") as f:
        f.write(data)
    # 读取文件
    with open(file_name, "rb") as f:
        _ = f.read()
    end_time = time.time()

    # 删除生成的文件
    if os.path.exists(file_name):
        os.remove(file_name)  # 删除临时文件

    execution_time = end_time - start_time
    score = BASELINE_IO / execution_time * 100
    return execution_time, score


# 运行所有测试并输出每个测试的结果
def run_all_tests():
    single_core_time, single_core_score = single_core_test()
    multi_core_time, multi_core_score = multi_core_test()
    matrix_time, matrix_score = matrix_test()
    memory_time, memory_score = memory_bandwidth_test()
    float_time, float_score = floating_point_test()
    integer_time, integer_score = integer_calculation_test()
    thread_time, thread_score = thread_switching_test()
    sort_time, sort_score = sorting_test()
    compress_time, compress_score = compression_test()
    io_time, io_score = file_io_test()

    # 输出每个测试的详细信息
    print(f"单核性能: {single_core_time:.4f} 秒，得分: {single_core_score:.2f}")
    print(f"多核性能: {multi_core_time:.4f} 秒，得分: {multi_core_score:.2f}")
    print(f"矩阵计算性能: {matrix_time:.4f} 秒，得分: {matrix_score:.2f}")
    print(f"内存带宽性能: {memory_time:.4f} 秒，得分: {memory_score:.2f}")
    print(f"浮点运算性能: {float_time:.4f} 秒，得分: {float_score:.2f}")
    print(f"整数计算性能: {integer_time:.4f} 秒，得分: {integer_score:.2f}")
    print(f"线程切换性能: {thread_time:.4f} 秒，得分: {thread_score:.2f}")
    print(f"排序算法性能: {sort_time:.4f} 秒，得分: {sort_score:.2f}")
    print(f"压缩/解压缩性能: {compress_time:.4f} 秒，得分: {compress_score:.2f}")
    print(f"文件 I/O 性能: {io_time:.4f} 秒，得分: {io_score:.2f}")


if __name__ == "__main__":
    run_all_tests()  # 运行所有测试
