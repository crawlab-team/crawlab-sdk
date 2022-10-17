export declare interface ResultService {
  saveItem(...items: ResultItem[]): Promise<void>;

  saveItems(items: ResultItem[]): Promise<void>;

  save(items: ResultItem[]): Promise<void>;
}

export declare interface ResultItem {
  [key: string]: any;
}

export declare type SaveItemFn = (...items: ResultItem[]) => void;

export declare type SaveItemsFn = (items: ResultItem[]) => void;
