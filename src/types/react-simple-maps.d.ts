declare module 'react-simple-maps' {
  import { ComponentType, ReactNode } from 'react';

  interface GeoProps {
    key?: string;
    geography: any;
    fill?: string;
    stroke?: string;
    style?: {
      default?: Record<string, any>;
      hover?: Record<string, any>;
      pressed?: Record<string, any>;
    };
    onClick?: (geo: any) => void;
    onMouseEnter?: (geo: any) => void;
    onMouseLeave?: (geo: any) => void;
  }

  interface MarkerProps {
    coordinates: [number, number];
    children?: ReactNode;
  }

  export const ComposableMap: ComponentType<{
    projectionConfig?: Record<string, any>;
    width?: number;
    height?: number;
    style?: Record<string, any>;
    children?: ReactNode;
  }>;

  export const Geographies: ComponentType<{
    geography: string;
    children: (props: { geographies: any[] }) => ReactNode;
  }>;

  export const Geography: ComponentType<GeoProps>;

  export const Marker: ComponentType<MarkerProps>;
}
