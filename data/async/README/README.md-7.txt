<span class="pl-k">ListenableFuture<<span class="pl-smi">Response</span>></span> whenResponse <span class="pl-k">=</span> <span class="pl-k">???</span>;
<span class="pl-smi">Runnable</span> callback <span class="pl-k">=</span> () <span class="pl-k">-</span><span class="pl-k">></span> {
	<span class="pl-k">try</span>  {
		<span class="pl-smi">Response</span> response <span class="pl-k">=</span> whenResponse<span class="pl-k">.</span>get();
		<span class="pl-smi">System</span><span class="pl-k">.</span>out<span class="pl-k">.</span>println(response);
	} <span class="pl-k">catch</span> (<span class="pl-smi">InterruptedException</span> <span class="pl-k">|</span> <span class="pl-smi">ExecutionException</span> e) {
		e<span class="pl-k">.</span>printStackTrace();
	}
};
<span class="pl-smi">java.util.concurrent<span class="pl-k">.</span>Executor</span> executor <span class="pl-k">=</span> <span class="pl-k">???</span>;
whenResponse<span class="pl-k">.</span>addListener(() <span class="pl-k">-</span><span class="pl-k">></span> <span class="pl-k">???</span>, executor);