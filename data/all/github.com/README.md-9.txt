<span class="pl-k">CompletableFuture<<span class="pl-smi">Response</span>></span> whenResponse <span class="pl-k">=</span> asyncHttpClient
            .prepareGet(<span class="pl-s"><span class="pl-pds">"</span>http://www.example.com/<span class="pl-pds">"</span></span>)
            .execute()
            .toCompletableFuture()
            .exceptionally(t <span class="pl-k">-</span><span class="pl-k">></span> { <span class="pl-c"><span class="pl-c">/*</span> Something wrong happened... <span class="pl-c">*/</span></span>  } )
            .thenApply(response <span class="pl-k">-</span><span class="pl-k">></span> { <span class="pl-c"><span class="pl-c">/*</span>  Do something with the Response <span class="pl-c">*/</span></span> <span class="pl-k">return</span> resp; });
whenResponse<span class="pl-k">.</span>join(); <span class="pl-c"><span class="pl-c">//</span> wait for completion</span>